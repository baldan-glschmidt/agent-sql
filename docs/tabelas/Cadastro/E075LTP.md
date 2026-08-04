# E075LTP

## Descrição

Cadastros - Integrações - Sapiens Varejo - Produto X Transação

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| CodTns | String(005) | Não | Transação de venda a consumidor final |
| TnsEdv | String(005) | Sim | Transação de entrada por devolução de venda |
| ImpDcp | String(001) | Sim | Indicativo se deve imprimir a descrição completa |
| SitReg | String(001) | Não | Situação do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer

---

## Índices

### E075LTPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E075LTP_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

