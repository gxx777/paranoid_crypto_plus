# Google Paranoid Plus

本项目基于[google paranoid crypto](https://github.com/google/paranoid_crypto) 项目，该项目可以检查**RSA**、**ECDSA**、**EC**公钥的弱参数以及伪随机数发生器。

修改了 example 文件下的

- [ec_public_keys.py](https://github.com/google/paranoid_crypto/blob/main/examples/ec_public_keys.py)
- [ecdsa_signatures.py](https://github.com/google/paranoid_crypto/blob/main/examples/ecdsa_signatures.py)
- [rsa_public_keys.py](https://github.com/google/paranoid_crypto/blob/main/examples/rsa_public_keys.py)

实现可以直接通过网站证书使用该工具。

[**paranoid_crypto**]  https://github.com/google/paranoid_crypto 

[**Google Security Blog**]  https://security.googleblog.com/2022/08/announcing-open-sourcing-of-paranoids.html 

# Getting Started

安装同[google paranoid crypto](https://github.com/google/paranoid_crypto) 

克隆存储库：

```
$ git clone https://github.com/gxx777/paranoid_crypto_plus.git && cd paranoid_crypto_plus
```

**注意**：以下命令已在 Debian 最新稳定版本 (bullseye) 上进行了测试。确保您将使用`python3.9`或更新。

安装依赖项：

```
$ sudo apt update && sudo apt install python3 python3-pip python3-pybind11 python3-fpylll libgmp-dev protobuf-compiler
```

安装 paranoid_crypto python 包：

```
$ python3 -m pip install .
```

要检查安装是否成功，您可以运行单元测试。例如：

```
$ cd paranoid_crypto_plus && python3 -m unittest discover -b -p "*test.py"
.................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 305 tests in 314.660s

OK
```



# Usage

Warnning the running dictory must be `examples`,so you should run `cd examples` first!

**另需安装OpenSSL** 

## 1. RSA

需要提供RSA的两个参数(e,n) 做测试 ,已支持从证书中获取

```shell
python3 rsa_public_keys.py --target pemfile_path
```

**e.g.**

```
ubuntu@ubuntu-virtual-machine:~/paranoid_crypto_plus/examples$ python3 rsa_public_keys.py --target /home/ubuntu/Downloads/baidu-com.pem
I1105 20:54:14.435781 140600795275264 paranoid.py:199] -------- Testing 1 RSA keys --------
I1105 20:54:15.307752 140600795275264 default_storage.py:55] Loading Keypair data from lib/data/keypair_table_small.lzma.
I1105 20:54:15.348662 140600795275264 paranoid.py:171] CheckSizes                     passed                    (0.00s)
I1105 20:54:15.348776 140600795275264 paranoid.py:171] CheckExponents                 passed                    (0.00s)
I1105 20:54:15.348891 140600795275264 paranoid.py:171] CheckROCA                      passed                    (0.00s)
I1105 20:54:15.348972 140600795275264 paranoid.py:171] CheckROCAVariant               passed                    (0.00s)
I1105 20:54:15.363067 140600795275264 paranoid.py:171] CheckFermat                    passed                    (0.01s)
I1105 20:54:15.363149 140600795275264 paranoid.py:171] CheckHighAndLowBitsEqual       passed                    (0.00s)
I1105 20:54:15.363425 140600795275264 paranoid.py:171] CheckOpensslDenylist           passed                    (0.00s)
I1105 20:54:15.367277 140600795275264 paranoid.py:171] CheckContinuedFractions        passed                    (0.00s)
I1105 20:54:15.425516 140600795275264 paranoid.py:171] CheckBitPatterns               passed                    (0.06s)
I1105 20:54:15.427759 140600795275264 paranoid.py:171] CheckPermutedBitPatterns       passed                    (0.00s)
I1105 20:54:15.428755 140600795275264 paranoid.py:171] CheckPollardpm1                passed                    (0.00s)
I1105 20:54:15.466361 140600795275264 paranoid.py:171] CheckLowHammingWeight          passed                    (0.04s)
I1105 20:54:15.508099 140600795275264 paranoid.py:171] CheckUnseededRand              passed                    (0.04s)
I1105 20:54:15.509759 140600795275264 paranoid.py:171] CheckSmallUpperDifferences     passed                    (0.00s)
I1105 20:54:15.509865 140600795275264 paranoid.py:171] CheckKeypairDenylist           passed                    (0.00s)
I1105 20:54:15.509990 140600795275264 paranoid.py:171] CheckGCD                       passed                    (0.00s)
I1105 20:54:15.510085 140600795275264 paranoid.py:171] CheckGCDN1                     passed                    (0.00s)
I1105 20:54:15.510148 140600795275264 paranoid.py:179] final state: passed
I1105 20:54:15.510212 140600795275264 paranoid.py:180] total time: 0.16s
I1105 20:54:15.510314 140600795275264 rsa_public_keys.py:133] Found first key to be potentially weak? False
```





## 2.  EC

需要提供ECC公钥的信息（r，s），已支持从证书中获取

```python
python3 ec_public_keys.py --target pemfile_path
```

**e.g.**

```shell
ubuntu@ubuntu-virtual-machine:~/paranoid_crypto_plus/examples$ python3 ec_public_keys.py --target /home/ubuntu/Downloads/github-com.pem
I1105 20:45:04.124772 140498963496960 paranoid.py:217] -------- Testing 1 EC keys --------
I1105 20:45:04.125140 140498963496960 paranoid.py:171] CheckValidECKey                passed                    (0.00s)
I1105 20:45:04.125244 140498963496960 paranoid.py:171] CheckWeakCurve                 passed                    (0.00s)
I1105 20:45:04.903296 140498963496960 paranoid.py:171] CheckWeakECPrivateKey          passed                    (0.78s)
I1105 20:45:04.903486 140498963496960 paranoid.py:171] CheckECKeySmallDifference      passed                    (0.00s)
I1105 20:45:04.903543 140498963496960 paranoid.py:179] final state: passed
I1105 20:45:04.903620 140498963496960 paranoid.py:180] total time: 0.78s
I1105 20:45:04.903680 140498963496960 ec_public_keys.py:143] Found first key to be potentially weak? False
```

## 3. ECDSA

针对ECDSA签名，需要5个参数。分别为(r，s) 作为签名者。m的Hash值。签发者的公钥(x,y)。支持独立模式和证书链模式

### (1) 独立模式

```shell
python3 ecdsa_signatures.py --target cert.pem --issuer_target issuer.pem
```

**e.g.**

```shell
ubuntu@ubuntu-virtual-machine:~/paranoid_crypto_plus/examples$ python3 ecdsa_signatures.py --target cert_temp0.pem --issuer_target cert_temp1.pem
cert_name: cert_temp0.pem
issuer_cert_name: cert_temp1.pem
记录了1245+0 的读入
记录了1245+0 的写出
1245字节（1.2 kB，1.2 KiB）已复制，0.00151709 s，821 kB/s
    0:d=0  hl=2 l=  70 cons: SEQUENCE          
    2:d=1  hl=2 l=  33 prim: INTEGER           :C02E5865D8F0A69359B4771194403DCD06C0908879027F7F8AC06F610A7BF067
   37:d=1  hl=2 l=  33 prim: INTEGER           :955D371BD746D3CE01ADD2178DC7B7A56541BA85366CF2AFA7E8A4591A6A1D42
I1105 20:55:42.901800 140645909024768 paranoid.py:236] -------- Testing 1 ECDSA signatures --------
I1105 20:55:42.954903 140645909024768 paranoid.py:171] CheckLCGNonceGMP               passed                    (0.05s)
I1105 20:55:43.632992 140645909024768 paranoid.py:171] CheckLCGNonceJavaUtilRandom    passed                    (0.68s)
I1105 20:55:43.636664 140645909024768 paranoid.py:171] CheckNonceMSB                  passed                    (0.00s)
I1105 20:55:43.636971 140645909024768 paranoid.py:171] CheckNonceCommonPrefix         passed                    (0.00s)
I1105 20:55:43.637224 140645909024768 paranoid.py:171] CheckNonceCommonPostfix        passed                    (0.00s)
I1105 20:55:43.637499 140645909024768 paranoid.py:171] CheckNonceGeneralized          passed                    (0.00s)
I1105 20:55:44.372894 140645909024768 paranoid.py:171] CheckIssuerKey                 passed                    (0.74s)
I1105 20:55:44.375970 140645909024768 paranoid.py:171] CheckCr50U2f                   passed                    (0.00s)
I1105 20:55:44.376049 140645909024768 paranoid.py:179] final state: passed
I1105 20:55:44.376144 140645909024768 paranoid.py:180] total time: 1.47s
I1105 20:55:44.376217 140645909024768 ecdsa_signatures.py:338] Found first signature to be potentially weak? False
```

### (2) 证书链模式

```
python3 ecdsa_signatures.py --cert_chains cert-chains.pem 
```

**e.g.**

```shell
ubuntu@ubuntu-virtual-machine:~/paranoid_crypto_plus/examples$ python3 ecdsa_signatures.py --cert_chains /home/ubuntu/Downloads/xxxxx.pem 
<absl.flags._flagvalues.FlagHolder object at 0x7f2fadfc3d90>
记录了1243+0 的读入
记录了1243+0 的写出
1243字节（1.2 kB，1.2 KiB）已复制，0.00143563 s，866 kB/s
    0:d=0  hl=2 l=  69 cons: SEQUENCE          
    2:d=1  hl=2 l=  32 prim: INTEGER           :67A098B33E286C3A6DCD8CB88594F3FE193D286A97F346F6DEA90B40B84D092F
   36:d=1  hl=2 l=  33 prim: INTEGER           :BB82BF072F06EE4904E3DF46156BC6AEA40046D6EDA55CF045DC7D55B09B3C55
I1105 20:59:33.482460 139842785869824 paranoid.py:236] -------- Testing 1 ECDSA signatures --------
I1105 20:59:33.525966 139842785869824 paranoid.py:171] CheckLCGNonceGMP               passed                    (0.04s)
I1105 20:59:34.216347 139842785869824 paranoid.py:171] CheckLCGNonceJavaUtilRandom    passed                    (0.69s)
I1105 20:59:34.219581 139842785869824 paranoid.py:171] CheckNonceMSB                  passed                    (0.00s)
I1105 20:59:34.219884 139842785869824 paranoid.py:171] CheckNonceCommonPrefix         passed                    (0.00s)
I1105 20:59:34.220174 139842785869824 paranoid.py:171] CheckNonceCommonPostfix        passed                    (0.00s)
I1105 20:59:34.220469 139842785869824 paranoid.py:171] CheckNonceGeneralized          passed                    (0.00s)
I1105 20:59:34.959105 139842785869824 paranoid.py:171] CheckIssuerKey                 passed                    (0.74s)
I1105 20:59:34.962246 139842785869824 paranoid.py:171] CheckCr50U2f                   passed                    (0.00s)
I1105 20:59:34.962372 139842785869824 paranoid.py:179] final state: passed
I1105 20:59:34.962450 139842785869824 paranoid.py:180] total time: 1.48s
I1105 20:59:34.962510 139842785869824 ecdsa_signatures.py:338] Found first signature to be potentially weak? False
```

## 4. Randonness

随机数发生器需要自己定suite才可以测试
### 1). 定义suite

目前up还是在python3的`site-packages` 中修改，因当前目录中`paranoid_crypto`修改后无效果，猜测是python的解析包没有做链接用的是`.local/lib` 下面的`paranoid_crypto`包。

具体修改地址为： (不同系统可能路径不同，本质是python 包的地址)

`/home/ubuntu/.local/lib/python3.10/site-packages/paranoid_crypto/lib/randomness_tests/rng.py`

------

**在rng.py 文件中定义测试用例**

**e.g.**

```python
class Prandom(Rng):
  """
  use python random.random to generator

  """
  def RandomBits(self, n: int, *, seed: Optional[int] = None) -> int:
    """Generates random bits.

    Args:
      n: the number of bits to generate.
      seed: a seed to initialize the pseudorandom number generator. Should be
        used for testing only. If the seed is None then the pseudorandom number
        generator is seeded randomly and subsequent calls to this function
        return unrelated results.

    Returns:
      an integer in the range 0 .. 2**n - 1
    """
    random.seed(seed)
    if n == 0:
      return 0
    else:
      return random.randint(1,2**n-1)
  
```

### 2).添加自定义套件到source

将新添加的测试用例加入到 `rng.py` 的 `RNGS`列表中

```python
RNGS = {
    "urandom": Urandom(),
    "Prandom":Prandom(),
    "mt19937": Mt19937(),
    "shake128": Shake128(),
    "gmp16": GmpRand(16),
    "gmp20": GmpRand(20),
    "gmp28": GmpRand(28),
    "gmp32": GmpRand(32),
    "gmp64": GmpRand(64),
    "gmp128": GmpRand(128),
    "mwc64": Mwc(2**64 - 742, 2**64),
    "mwc128": Mwc(2**128 - 10480, 2**128),
    "mwc256": Mwc(2**256 - 9166, 2**256),
    "mwc512": Mwc(2**512 - 150736, 2**512),
    "lehmer128": Lehmer(),
    "lehmer128/16": Lehmer(bits=16),
    "lehmer128/8": Lehmer(bits=8),
    "xorshift128+": XorShift128plus(),
    "xorshift*": XorShiftStar(),
    "xorwow": Xorwow(),
    "java": JavaRandom(),
    "lcgnist": LcgNist(),
    "pcg64": Pcg64(),
    "philox": Philox(),
    "sfc64": Sfc64(),
    "subsetsum256/16": SubsetSum(256, 16),
    "subsetsum256/24": SubsetSum(256, 24),
    "subsetsum256/32": SubsetSum(256, 32),
    "subsetsum256/40": SubsetSum(256, 40),
    "subsetsum256/48": SubsetSum(256, 48),
    "subsetsum512/56": SubsetSum(512, 56),
    "subsetsum512/64": SubsetSum(512, 64),
    "subsetsum1024/64": SubsetSum(1024, 64),
}

```

### 3).运行 --source

```shell
python3 randomness.py --source Prandom
```

**e.g.**

```shell
ubuntu@ubuntu-virtual-machine:~/paranoid_crypto_plus/examples$ python3 randomness.py --source Prandom
_SOURCE.value:  Prandom
I1105 21:16:22.832049 140172271603712 random_test_suite.py:295] -------- Testing: Prandom --------
I1105 21:16:22.832220 140172271603712 random_test_suite.py:297] number of bits: 10000000
I1105 21:16:22.866006 140172271603712 random_test_suite.py:230] Frequency                      passed: p=0.527089        (0.00s)
I1105 21:16:22.867743 140172271603712 random_test_suite.py:230] BlockFrequency                 passed: p=0.458889        (0.00s)
I1105 21:16:22.868851 140172271603712 random_test_suite.py:230] Runs                           passed: p=0.269148        (0.00s)
I1105 21:16:22.874467 140172271603712 random_test_suite.py:230] LongestRuns                    passed: p=0.798733        (0.01s)
I1105 21:16:23.298801 140172271603712 random_test_suite.py:230] BinaryMatrixRank               passed: p=0.664144        (0.42s)
I1105 21:16:26.390001 140172271603712 random_test_suite.py:230] Spectral                       passed: p=0.565577        (3.09s)
I1105 21:16:26.681255 140172271603712 random_test_suite.py:230] OverlappingTemplateMatching    passed: p=0.823404        (0.03s)
I1105 21:16:27.324736 140172271603712 random_test_suite.py:230] Universal                      passed: p=0.725476        (0.64s)
I1105 21:16:27.443893 140172271603712 random_test_suite.py:230] LinearComplexity [512]         passed: 2                 (0.12s)
I1105 21:16:27.586624 140172271603712 random_test_suite.py:230] LinearComplexity [1024]        passed: 2                 (0.14s)
I1105 21:16:27.814236 140172271603712 random_test_suite.py:230] LinearComplexity [2048]        passed: 2                 (0.23s)
I1105 21:16:28.222768 140172271603712 random_test_suite.py:230] LinearComplexity [4096]        passed: 2                 (0.41s)
I1105 21:16:29.618798 140172271603712 random_test_suite.py:230] Serial                         passed: 38                (1.40s)
I1105 21:16:30.042774 140172271603712 random_test_suite.py:230] ApproximateEntropy             passed: 14                (0.42s)
I1105 21:16:30.677173 140172271603712 random_test_suite.py:230] RandomWalk                     passed: 28                (0.63s)
I1105 21:16:30.740490 140172271603712 random_test_suite.py:230] LargeBinaryMatrixRank          passed: 6                 (0.06s)
I1105 21:16:33.260365 140172271603712 random_test_suite.py:230] LinearComplexityScatter [32, 100000] failed: p=0               (2.52s)
/home/ubuntu/.local/lib/python3.10/site-packages/scipy/stats/_discrete_distns.py:82: RuntimeWarning: divide by zero encountered in _binom_cdf
  return _boost._binom_cdf(k, n, p)
I1105 21:16:34.684052 140172271603712 random_test_suite.py:230] LinearComplexityScatter [64, 50000] failed: p=0               (1.42s)
I1105 21:16:36.572060 140172271603712 random_test_suite.py:230] LinearComplexityScatter [128, 40000] failed: p=0               (1.89s)
I1105 21:16:38.028176 140172271603712 random_test_suite.py:230] FindBias [256]                 passed: p=0.259713        (1.46s)
I1105 21:16:40.602871 140172271603712 random_test_suite.py:230] FindBias [384]                 passed: p=0.675782        (2.57s)
I1105 21:16:45.335655 140172271603712 random_test_suite.py:230] FindBias [512]                 passed: p=0.035322        (4.73s)
I1105 21:16:58.081303 140172271603712 random_test_suite.py:230] FindBias [1024]                passed: p=0.014096        (12.75s)
I1105 21:16:58.370356 140172271603712 random_test_suite.py:230] NonOverlappingTemplateMatching passed: 284               (0.27s)
I1105 21:16:58.370640 140172271603712 random_test_suite.py:263] passed    : 390/393
I1105 21:16:58.370692 140172271603712 random_test_suite.py:263] failed    : 3/393
I1105 21:16:58.370724 140172271603712 random_test_suite.py:328] total time: 35.54s
```




# Reference

[1] https://github.com/google/paranoid_crypto

[2] https://blog.yuantops.com/tech/validate_a_digital_certificate_step_by_step/