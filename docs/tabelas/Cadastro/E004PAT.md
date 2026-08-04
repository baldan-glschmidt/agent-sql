# E004PAT

## Descrição

Tabelas - Parâmetros - Simulação de Transferência de Saldos Bancários

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| AbgEmp | String(250) | Sim | Códigos das empresas solicitadas |
| AbgFil | String(250) | Sim | Códigos das filiais solicitadas |
| AbgAbf | String(250) | Sim | Códigos das abrangências de filiais solicitadas |
| DatSal | Date | Não | Data base para saldo das contas |
| DatMov | Date | Não | Data para movimentações de tranferências entre contas |
| CxbCco | String(250) | Sim | Abrangência das contas internas |
| CxbNcc | String(001) | Sim | Indicativo se deve negar abrangência de contas internas solicitadas |
| CxbTcc | String(250) | Sim | Abrangência dos tipos de contas internas |
| CxbNtc | String(001) | Sim | Indicativo se deve negar abrangência de tipos de contas solicitados |
| CxbFil | String(250) | Sim | Abrangência das filiais das contas internas |
| CxbNfi | String(001) | Sim | Indicativo se deve negar abrangência de filiais das contas solicitadas |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
