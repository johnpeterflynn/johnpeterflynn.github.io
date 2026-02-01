document.addEventListener("nav", () => {
  const emailEl = document.getElementById("hero-email")
  if (emailEl) {
    const u = "john"
    const d = "johnpeterflynn.com"
    emailEl.innerHTML = `<a href="mailto:${u}@${d}">${u}@${d}</a>`
  }
})
