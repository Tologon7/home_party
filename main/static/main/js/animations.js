AOS.init({
  duration: 1400,
  once: true,
  easing: 'ease-in-out-cubic'
});


(function () {
  const audio = document.getElementById('bg-music');
  if (!audio) return;

  let started = false;

  document.addEventListener('click', function () {
    if (started) return;

    audio.play()
      .then(() => {
        console.log('Audio started');
        started = true;
      })
      .catch(err => {
        console.log('Play blocked:', err);
      });
  });
})();
