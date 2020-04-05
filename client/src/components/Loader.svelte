<div class="loader-container">
    <div class="overflow"/>
    <div class="lds-hourglass"></div>
</div>
<style>
.loader-container {
    position: fixed;
    width: 100vw;
    display: flex;
    height: 100vh;
    justify-content: center;
    align-items: center;
}
.overflow{
    position: fixed;
    width: 100vw;
    height: 100vh;
    background: #EAEAEA;
    opacity: .5;
}
.lds-hourglass {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-hourglass:after {
  content: " ";
  display: block;
  border-radius: 50%;
  width: 0;
  height: 0;
  margin: 8px;
  box-sizing: border-box;
  border: 32px solid var(--secondary-text);
  border-color: var(--secondary-text) transparent var(--secondary-text) transparent;
  animation: lds-hourglass 1.2s infinite;
}
@keyframes lds-hourglass {
  0% {
    transform: rotate(0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  50% {
    transform: rotate(900deg);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  100% {
    transform: rotate(1800deg);
  }
}
</style>