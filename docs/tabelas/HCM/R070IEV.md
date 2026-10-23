# R070IEV

## Descrição

Imagens do evento da câmera CFTV

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| DatAcc | Date | Não | Data Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqAcc | Number(002,0) | Não | Sequência do Registro |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| Camera | Number(005,0) | Não | Câmera CFTV |
| ImgCap | String(001) | Não | Imagem do Acesso Capturada |
| ImgCam | Image | Sim | Imagem da câmera |
| ImgDir | String(256) | Sim | Diretório da Imagem da câmera |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc
- CodDsp
- Camera

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
