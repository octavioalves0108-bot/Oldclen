// Validação no cliente e envio do formulário de login.
// A validação aqui é só para experiência do usuário; a verificação que vale
// é a do servidor. A senha nunca é guardada, logada ou enviada para além da
// requisição de login para o próprio backend.

const form = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const submitBtn = document.getElementById('submit');
const banner = document.getElementById('banner');
const toggleBtn = document.getElementById('toggle-password');
const loggedView = document.getElementById('logged-view');
const loggedName = document.getElementById('logged-name');
const logoutBtn = document.getElementById('logout');

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function showBanner(message, type) {
  banner.textContent = message;
  banner.classList.remove('is-error', 'is-success');
  banner.classList.add(type === 'error' ? 'is-error' : 'is-success');
  banner.hidden = false;
}

function clearBanner() {
  banner.hidden = true;
  banner.textContent = '';
}

function setFieldError(input, message) {
  const field = input.closest('.field');
  const errorEl = document.getElementById(`${input.id}-error`);
  if (message) {
    field.classList.add('invalid');
    input.setAttribute('aria-invalid', 'true');
    if (errorEl) errorEl.textContent = message;
  } else {
    field.classList.remove('invalid');
    input.removeAttribute('aria-invalid');
    if (errorEl) errorEl.textContent = '';
  }
}

function validateEmail() {
  const value = emailInput.value.trim();
  if (!value) return setFieldError(emailInput, 'Informe seu e-mail.'), false;
  if (!EMAIL_RE.test(value)) return setFieldError(emailInput, 'E-mail inválido.'), false;
  setFieldError(emailInput, '');
  return true;
}

function validatePassword() {
  const value = passwordInput.value;
  if (!value) return setFieldError(passwordInput, 'Informe sua senha.'), false;
  if (value.length < 8) return setFieldError(passwordInput, 'A senha tem no mínimo 8 caracteres.'), false;
  setFieldError(passwordInput, '');
  return true;
}

emailInput.addEventListener('blur', validateEmail);
passwordInput.addEventListener('blur', validatePassword);
emailInput.addEventListener('input', () => {
  if (emailInput.closest('.field').classList.contains('invalid')) validateEmail();
});
passwordInput.addEventListener('input', () => {
  if (passwordInput.closest('.field').classList.contains('invalid')) validatePassword();
});

// Mostrar / ocultar senha
toggleBtn.addEventListener('click', () => {
  const showing = passwordInput.type === 'text';
  passwordInput.type = showing ? 'password' : 'text';
  toggleBtn.setAttribute('aria-pressed', String(!showing));
  toggleBtn.setAttribute('aria-label', showing ? 'Mostrar senha' : 'Ocultar senha');
  toggleBtn.querySelector('span').textContent = showing ? 'Mostrar' : 'Ocultar';
});

function setLoading(loading) {
  submitBtn.disabled = loading;
  submitBtn.classList.toggle('loading', loading);
}

function renderLoggedIn(user) {
  form.hidden = true;
  document.querySelector('.switch').hidden = true;
  loggedName.textContent = user.displayName || user.email;
  loggedView.hidden = false;
}

function renderLoggedOut() {
  form.hidden = false;
  document.querySelector('.switch').hidden = false;
  loggedView.hidden = true;
  form.reset();
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  clearBanner();

  const okEmail = validateEmail();
  const okPassword = validatePassword();
  if (!okEmail || !okPassword) return;

  setLoading(true);
  try {
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify({
        email: emailInput.value.trim(),
        password: passwordInput.value,
      }),
    });

    let data = {};
    try {
      data = await res.json();
    } catch {
      /* resposta sem corpo JSON */
    }

    if (res.ok && data.ok) {
      showBanner(data.message || 'Login realizado com sucesso!', 'success');
      // Não guardamos a senha; limpamos o campo imediatamente.
      passwordInput.value = '';
      renderLoggedIn(data.user);
      return;
    }

    // Erros de campo vindos do servidor
    if (data.fields) {
      if (data.fields.email) setFieldError(emailInput, data.fields.email);
      if (data.fields.password) setFieldError(passwordInput, data.fields.password);
    }
    showBanner(data.error || 'Não foi possível entrar. Verifique os dados.', 'error');
  } catch {
    showBanner('Falha de conexão. Tente novamente.', 'error');
  } finally {
    setLoading(false);
  }
});

logoutBtn.addEventListener('click', async () => {
  try {
    await fetch('/api/logout', { method: 'POST', credentials: 'same-origin' });
  } catch {
    /* ignora */
  }
  clearBanner();
  renderLoggedOut();
});

// Ao abrir, verifica se já existe sessão ativa.
(async function checkSession() {
  try {
    const res = await fetch('/api/me', { credentials: 'same-origin' });
    if (res.ok) {
      const data = await res.json();
      if (data.ok && data.user) renderLoggedIn(data.user);
    }
  } catch {
    /* sem sessão; segue com o formulário */
  }
})();
