function shuffle(arr)
{
    for (let i = arr.length-1; i > 0; i--)
    {
        // Gets a random number
        let n = randomNumber(i);

        // Interchanges the position of the value
        [arr[n], arr[i]] = [arr[i], arr[n]];
    }
    return arr;
}




























/**
 * Shuffles an array using the Fisher-Yates algorithm
 * Source: https://w.wiki/8Zj
 * 
 * @param {Array} arr 
 * @returns 
 */










function randomNumber(max, min=0)
{
    const num = Math.floor(Math.random() * (max - min)) + min;
    return num;
}























let leList = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];

const shuffleBtn = document.querySelector("#shuffle-btn");
const shuffleDisplaySegments = document.querySelectorAll(".shuffle-display__segment");

shuffleBtn.addEventListener("click", shuffleLoop);


async function shuffleLoop() {
    for (let i = 0; i < 7; i++) {
        await sleep(100)
        reshuffleDisplay()
    }
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms))

function reshuffleDisplay() {
    const shf = shuffle(leList);
    for (let i = 0; i < 10; i++) {
        shuffleDisplaySegments[i].textContent = shf[i];
    }
}
