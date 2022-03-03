# blackhobby
Automation program for printing label

## 개요
<pre>
이 프로젝트는 label 프린터를 조작할 때 하나씩 해야하는 번거로움을 줄이기 위해 시작한 프로젝트이다.
원래 사용하던 label 프린트 프로그램은 사진을 하나씩 옮겨 붙여넣어야 해서 주문 건이 수 십~ 수 백개에
달할 때에는 사진을 옮기는 작업 시간이 오래 걸렸다.

이를 해결하기 위해 프로그램을 만들었다.
</pre> 

## 주요 라이브러리 Version
<pre>
  openpyxl==3.0.9
  pandas==1.4.0
  Pillow==9.0.1
  pyinstaller==4.9
  PyQt5==5.15.6
</pre>

## 프로그램 실행 과정
### 1. 파일 열기
![1](https://user-images.githubusercontent.com/69226800/156506647-c10a0dc2-2015-4dfc-840e-3a771ddb89cc.JPG)
![2](https://user-images.githubusercontent.com/69226800/156506853-46c0055d-bdc5-4e95-8e0c-a7efc73c141f.JPG)

### 2. 파일 변환(이미지를 90도 눕혀서 Excel에 들어가기 쉽도록 변환해서 저장)
![3](https://user-images.githubusercontent.com/69226800/156506863-97b63079-ebd6-48c8-b80b-edeb4e2bf3d8.JPG)
![4](https://user-images.githubusercontent.com/69226800/156506864-c1cc0da1-50bf-4622-ab4b-e8c1746320fa.JPG)

### 3. Excel 파일 생성(주문 건에 대해 이미지 파일을 순서대로 붙여넣은 라벨을 프린트 할 수 있도록 조작 후 한 장씩 저장)
![5](https://user-images.githubusercontent.com/69226800/156506865-14505f52-fbca-44b5-acac-a0e7aad52d58.JPG)
![6](https://user-images.githubusercontent.com/69226800/156506868-46bb70a0-485b-4194-8d97-80da7011687b.JPG)

### 4. 저장한 Excel 파일 열어서 확인
![7](https://user-images.githubusercontent.com/69226800/156506869-eedbd621-427c-49fd-a7d0-58f92f5f4742.JPG)
