const cb = (delay1, delay_increment = 1, sum = 0) => {
    setTimeout(
      (delay2, sum) => {
        setTimeout(
          (delay3, sum) => {
            setTimeout(
              (sum) => {
                console.log(`got printed after ${sum} seconds`);
              },
              delay3,
              sum + delay3
            );
          },
          delay2,
          delay2 + delay_increment,
          sum + delay2
        );
      },
      delay1,
      delay1 + delay_increment,
      sum + delay1
    );
  };
  
  cb(1000);
  