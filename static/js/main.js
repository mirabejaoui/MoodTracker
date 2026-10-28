(function () {
  "use strict";

  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const isOpen = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!isOpen));
      nav.classList.toggle("is-open", !isOpen);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        toggle.focus();
      }
    });
  }

  document.querySelectorAll("[data-range]").forEach(function (input) {
    const output = document.querySelector('[data-range-output="' + input.id + '"]');
    if (!output) return;
    const update = function () { output.textContent = input.value + " / " + input.max; };
    input.addEventListener("input", update);
    update();
  });

  document.querySelectorAll("[data-dismissible]").forEach(function (alert) {
    const closeButton = alert.querySelector("[data-dismiss]");
    if (!closeButton) return;
    closeButton.addEventListener("click", function () {
      alert.classList.add("is-leaving");
      alert.addEventListener("transitionend", function () { alert.remove(); }, { once: true });
    });
  });

  document.querySelectorAll('.auth-card input[type="password"]').forEach(function (input) {
    const wrapper = document.createElement("div");
    wrapper.className = "password-field";
    input.parentNode.insertBefore(wrapper, input);
    wrapper.appendChild(input);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "password-toggle";
    button.textContent = "Show";
    button.setAttribute("aria-label", "Show password");
    button.setAttribute("aria-pressed", "false");
    wrapper.appendChild(button);

    button.addEventListener("click", function () {
      const isHidden = input.type === "password";
      input.type = isHidden ? "text" : "password";
      button.textContent = isHidden ? "Hide" : "Show";
      button.setAttribute("aria-label", isHidden ? "Hide password" : "Show password");
      button.setAttribute("aria-pressed", String(isHidden));
    });
  });
})();
