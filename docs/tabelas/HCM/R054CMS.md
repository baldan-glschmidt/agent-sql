# R054CMS

## Descrição

Compensações da GPS - Valores Compensados

---

## Resumo

- Campos: 17
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ComCmp | Date | Não | Competência da Compensação |
| OriCom | Number(001,0) | Não | Origem da Compensação |
| ComSld | Date | Não | Competência do Saldo |
| OriGps | Number(001,0) | Não | Origem da GPS em que o valor foi compensado |
| FilCom | Number(006,0) | Não | Filial da Compensação |
| RatCom | Number(009,0) | Não | Rateio da Compensação |
| ValCmp | Number(011,2) | Sim | Valor da Compensação |
| CorCmp | Number(011,2) | Sim | Valor da Correção da Compensação |
| ValSld | Number(011,2) | Sim | Valor do Saldo |
| CorSld | Number(011,2) | Sim | Valor da Correção do Saldo |
| OriReg | Number(001,0) | Sim | Origem Registro |
| TipPar | String(001) | Sim | Tipo Parâmetro |
| Cmp13s | Number(011,2) | Sim | Valor da Compensação do 13° Salário |
| Cor13s | Number(011,2) | Sim | Valor da Correção da Compensação do 13° Salário |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- ComCmp
- OriCom
- ComSld
- OriGps
- FilCom
- RatCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
