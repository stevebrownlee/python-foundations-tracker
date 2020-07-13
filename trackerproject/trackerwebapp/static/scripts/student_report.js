const scoreElements = document.querySelectorAll("classroomscore")

for (const scoreElement of scoreElements) {
    const scoreAttribute = scoreElement.getAttribute("score")
    const score = parseFloat(scoreAttribute)

    switch (true) {
        case ( score >= 80):
            scoreElement.classList.add("score--high")
            break;
        case (score >= 50 && score < 80):
            scoreElement.classList.add("score--warning")
            break;
        case (score < 50):
            scoreElement.classList.add("score--alert")
            break;
    }
}


const coll = document.getElementsByClassName("collapsible")
let i

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active")
        const content = this.nextElementSibling

        if (content.style.maxHeight) {
            content.style.maxHeight = null
        } else {
            content.style.maxHeight = content.scrollHeight + "px"
        }
    })
}