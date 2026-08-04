# E000BNF

## Descrição

Tabelas - Integrações - Situações Tributárias X Dispositivo Fiscal

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SigUfs | String(002) | Não | Sigla do estado |
| CodStr | String(003) | Não | Código da Situação Tributária ICMS |
| DatIni | Date | Não | Data de início da vigência |
| CodClf | String(003) | Não | Código da classificação fiscal |
| CodTns | String(005) | Não | Código da transação |
| CodPro | String(014) | Não | Código do produto |
| CodSer | String(014) | Não | Código do serviço |

---

## Chave Primária

- SeqInt

---

## Índices

### E000BNFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- SigUfs
- CodStr
- DatIni
- CodClf
- CodTns
- CodPro
- CodSer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
