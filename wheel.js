document.addEventListener('DOMContentLoaded', function() {
  const spinBtn = document.getElementById('spinbtn');
  const wheel = document.getElementById('wheel');
  const numSlices = 200;  // Number of prize slices
  const sliceDegrees = 360 / numSlices;  // Each slice spans 1.8 degrees (360 / 200)

  // Load game state from localStorage
  const prizeWon = localStorage.getItem('prizeWon');
  const hasPlayed = localStorage.getItem('hasPlayed');
  const totalWinners = parseInt(localStorage.getItem('totalWinners') || '0');  // Get the total number of winners
  const maxWinners = 200;  // Maximum number of winners allowed

  // If 200 people have already won or the player has already won, show the "Try Again" page
  if (totalWinners >= maxWinners) {
    window.location.href = 'tryagain.html';  // Redirect to all winners page if the max is reached
  } else if (prizeWon === 'true') {
    window.location.href = 'tryagain.html';  // Redirect if the player has already won
  } else if (hasPlayed === 'true') {
    window.location.href = 'tryagain.html';  // Redirect if the player has already played
  }

  spinBtn.addEventListener('click', function() {
    // Random spin duration between 1500ms and 3000ms
    const spinDuration = Math.floor(Math.random() * 2000) + 3000;
    const randomDegree = Math.floor(Math.random() * 360);
    const finalDegree = randomDegree + (360 * 3);  // 3 full rotations

    wheel.style.transition = `transform ${spinDuration}ms ease-out`;
    wheel.style.transform = `rotate(${finalDegree}deg)`;

    setTimeout(function() {
      // After the spin ends, calculate which slice landed on
      const landingDegree = finalDegree % 360;
      const landingSlice = Math.floor(landingDegree / sliceDegrees);

      // If player lands on Slice 4 (Prize), update prizeWon status
      if (landingSlice === 3) {  // Slice 4 is at index 3
        localStorage.setItem('prizeWon', 'true');
        localStorage.setItem('hasPlayed', 'true');
        // Update the total winners count
        let updatedTotalWinners = totalWinners + 1;
        localStorage.setItem('totalWinners', updatedTotalWinners.toString());

        // Optional: Display some feedback before redirecting
        setTimeout(function() {
          window.location.href = 'prize.html';
        }, 1000);  // Delay the redirect by 1 second for a better experience
      } else {
        localStorage.setItem('hasPlayed', 'true');
        setTimeout(function() {
          window.location.href = 'tryagain.html';
        }, 1000);  // Delay the redirect by 1 second
      }
    }, spinDuration);
  });
});
