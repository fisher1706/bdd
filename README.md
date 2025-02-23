# https://www.youtube.com/watch?v=x71yt24Hdqw&list=PLuGEX9IcSH_d4fc9Wich3TEma5UKyWBSt&index=1
# https://pypi.org/project/behave/

# start feature [demo_test_case.feature]
```shell
behave features/demo_test_case.feature
```

# start feature with tag [sanity]
```shell
behave --tags=sanity
```

# start all tests
```shell
behave
```

# generate allure -> settings for allure in [behave.ini]
```shell
allure serve
```