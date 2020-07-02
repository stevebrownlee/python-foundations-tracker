document.querySelector(".submissions").addEventListener("change", e => {
    if (e.target.classList.contains("cohortSelect")) {
        const chosenCohort = e.target.value

        if (chosenCohort !== "") {
            document.querySelector(`.cohortForm--${e.target.id.split("--")[1]}`).submit()
        }
    }
})