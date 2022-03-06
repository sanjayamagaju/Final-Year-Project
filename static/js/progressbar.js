const progress = document.querySelector(".progress-bar")

  console.log({{other_campaign.Collected}});
  console.log({{other_campaign.Target}});
  const progpercent = {{other_campaign.Collected}}/{{other_campaign.Target}};

  const interval = setInterval(() => {
    progress.style.width = `${progpercent * 100}%`;
  })