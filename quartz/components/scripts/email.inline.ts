document.addEventListener("nav", () => {
  const emailEl = document.getElementById("hero-email")
  if (emailEl) {
    const u = "johnflynn90"
    const d = "gmail.com"
    emailEl.innerHTML = `<a href="mailto:${u}@${d}">${u}@${d}</a>`
  }
})
