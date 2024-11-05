<script></script>

<template>
  <div class="container">
    <i v-for="n in 40" :key="n"></i>
  </div>
</template>

<style scoped>
.container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 95%;
  overflow: hidden;
  background-color: #000;
  z-index: -1;
  border-radius: 10px;
}

i {
  position: absolute;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  -webkit-animation: screen infinite;
  animation: screen infinite;
}

i:nth-child(1) {
  top: 20px;
  left: 30px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(2, 226, 252, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #02e2fc;
  animation-duration: 5s;
}

i:nth-child(2) {
  top: 420px;
  left: 30px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(250, 160, 2, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #faa002;
  animation-duration: 21s;
}

i:nth-child(3) {
  top: 550px;
  left: 880px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(20, 252, 2, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #14fc02;
  animation-duration: 5s;
}

i:nth-child(4) {
  top: 5px;
  left: 1030px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(252, 2, 196, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #fc02c4;
  animation-duration: 4s;
}

i:nth-child(5) {
  top: 280px;
  left: 12px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(139, 44, 148, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #8b2c94;
  animation-duration: 5s;
}

i:nth-child(6) {
  top: 550px;
  left: 30px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(251, 184, 41, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #fbb829;
  animation-duration: 6s;
}

i:nth-child(7) {
  top: 650px;
  left: 50px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(195, 255, 104, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #c3ff68;
  animation-duration: 15s;
}

i:nth-child(8) {
  top: 20px;
  left: 860px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 0, 102, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff0066;
  animation-duration: 5s;
}
i:nth-child(9) {
  top: 896px;
  left: 132px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 255, 0, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ffff00;
  animation-duration: 13s;
}

i:nth-child(10) {
  top: 578px;
  left: 357px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(127, 175, 27, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #7faf1b;
  animation-duration: 4s;
}

i:nth-child(11) {
  top: 380px;
  left: 230px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(1, 210, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #01d2ff;
  animation-duration: 5s;
}

i:nth-child(12) {
  top: 570px;
  left: 1100px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(237, 247, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #edf7ff;
  animation-duration: 6s;
}

i:nth-child(13) {
  top: 600px;
  left: 600px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(0, 255, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #00ffff;
  animation-duration: 7s;
}

i:nth-child(14) {
  top: 200px;
  left: 520px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(0, 0, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #0000ff;
  animation-duration: 14s;
}

i:nth-child(15) {
  top: 370px;
  left: 500px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(16, 225, 228, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #10e1e4;
  animation-duration: 9s;
}

i:nth-child(16) {
  top: 620px;
  left: 730px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 51, 0, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff3300;
  animation-duration: 3s;
}
i:nth-child(17) {
  top: 62px;
  left: 330px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 234, 232, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ffeae8;
  animation-duration: 4s;
}

i:nth-child(18) {
  top: 0px;
  left: 250px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 229, 0, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ffe500;
  animation-duration: 5s;
}

i:nth-child(19) {
  top: 600px;
  left: 180px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 102, 153, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff6699;
  animation-duration: 6s;
}

i:nth-child(20) {
  top: 987px;
  left: 13px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(84, 156, 204, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #549ccc;
  animation-duration: 7s;
}

i:nth-child(21) {
  top: 120px;
  left: 930px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(184, 175, 3, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #b8af03;
  animation-duration: 8s;
}

i:nth-child(22) {
  top: 80px;
  left: 700px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(171, 250, 249, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #abfaf9;
  animation-duration: 5s;
}

i:nth-child(23) {
  top: 350px;
  left: 720px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(127, 15, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #7f0fff;
  animation-duration: 2s;
}

i:nth-child(24) {
  top: 997px;
  left: 678px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(48, 128, 0, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #308000;
  animation-duration: 3s;
}

i:nth-child(25) {
  top: 714px;
  left: 246px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 38, 38, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff2626;
  animation-duration: 4s;
}

i:nth-child(26) {
  top: 0px;
  left: 480px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(15, 29, 215, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #0f1dd7;
  animation-duration: 5s;
}

i:nth-child(27) {
  top: 456px;
  left: 1000px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(51, 102, 153, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #336699;
  animation-duration: 6s;
}

i:nth-child(28) {
  top: 350px;
  left: 865px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(70, 172, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #46acff;
  animation-duration: 7s;
}

i:nth-child(29) {
  top: 100px;
  left: 100px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(222, 4, 5, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #de0405;
  animation-duration: 8s;
}

i:nth-child(30) {
  top: 1087px;
  left: 722px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(77, 254, 21, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #4dfe15;
  animation-duration: 9s;
}

i:nth-child(31) {
  width: 200px;
  height: 200px;
  top: 795px;
  left: 605px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(243, 10, 70, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #f30a46;
  animation-duration: 1s;
}

i:nth-child(32) {
  top: 234px;
  left: 678px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(245, 253, 45, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #f5fd2d;
  animation-duration: 2s;
}

i:nth-child(33) {
  top: 270px;
  left: 1230px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(178, 0, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #b200ff;
  animation-duration: 3s;
}
i:nth-child(34) {
  width: 200px;
  height: 200px;
  top: 1126px;
  left: 332px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(102, 204, 255, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #66ccff;
  -webkit-animation-duration: 4s;
  animation-duration: 4s;
}

i:nth-child(35) {
  top: 407px;
  left: 83px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(20, 243, 175, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #14f3af;
  animation-duration: 5s;
}

i:nth-child(36) {
  width: 200px;
  height: 200px;
  top: 176px;
  left: 297px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(100, 245, 102, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #64f566;
  animation-duration: 6s;
}

i:nth-child(37) {
  width: 300px;
  height: 300px;
  top: 820px;
  right: 10px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(236, 218, 65, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ecda41;
  animation-duration: 7s;
}

i:nth-child(38) {
  top: 500px;
  left: 500px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 61, 45, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff3d2d;
  animation-duration: 8s;
}

i:nth-child(39) {
  top: 20px;
  right: 26px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(74, 73, 235, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #4a49eb;
  animation-duration: 9s;
}

i:nth-child(40) {
  width: 200px;
  height: 200px;
  top: 251px;
  left: 1053px;
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(255, 72, 0, 0.65) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  box-shadow: 0px 0px 5px 0px #ff4800;
  animation-duration: 10s;
}

@keyframes screen {
  from {
    opacity: 0;
  }

  25% {
    opacity: 0.3;
    transform: scale3d(3, 3, 4);
  }

  50% {
    opacity: 0.75;
  }

  75% {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}
</style>
