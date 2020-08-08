<template>
  <img
    class="VuetifyLogo"
    alt="Vuetify Logo"
    src="https://res.cloudinary.com/musbell/image/upload/v1580986143/CORPAP3_btmvyg.png"
  />
</template>

<style>
.VuetifyLogo {
  width: 180px;
  transform: rotateY(560deg);
  animation: turn 3.5s ease-out forwards 1s;
}
@keyframes turn {
  100% {
    transform: rotateY(0deg);
  }
}
</style>
