cd ~/ab_ssrs_reporting_services/
git checkout -b dev_ssrs_reporting_services ab_ssrs_reporting_services
git commit -am "dev branch"
git checkout ab_ssrs_reporting_services
git merge --no-ff dev_ssrs_reporting_services
git push origin ab_ssrs_reporting_services
git push origin dev_ssrs_reporting_services
git push origin ab_ssrs_reporting_services:dev_ssrs_reporting_services
