function solution(polynomial) {
  const arr = polynomial.split(" ");
  let xNum = 0;
  let num = 0;

  arr.forEach((element) => {
    if (element === "+") {
      return;
    }

    if (element.includes("x")) {
      xNum = xNum + Number(element.split("x")[0] || 1);
    } else {
      num = num + Number(element);
    }
  });

  if (xNum === 1) {
    xNum = "";
  }

  if (xNum === 0 && num === 0) {
    return "0";
  } else if (xNum === 0) {
    return `${num}`;
  } else if (num === 0) {
    return `${xNum}x`;
  } else {
    return `${xNum}x + ${num}`;
  }
}
