# E000TPR

## Descrição

Tabelas - Integrações - Tabelas de preço

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do Produto (tamanho, cor, etc.) |
| CodSer | String(014) | Sim | Código do serviço |
| CodTpr | String(004) | Sim | Código da tabela de preço |
| DatIni | Date | Sim | Data validade inicial da tabela de preço |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TPRIndiceProduto

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodTpr
- DatIni

### E000TPRIndiceServico

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSer
- CodTpr
- DatIni

### E000TPRIndiceCompleto

**Tipo:** Unico

Campos:
- DatIni
- CodTpr
- CodSer
- CodDer
- CodPro
- CodFil
- CodEmp

### E000TPREmpresaFilial

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
