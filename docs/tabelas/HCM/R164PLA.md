# R164PLA

## Descrição

BS - Planos

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código da Seguradora |
| CodPla | Number(003,0) | Não | Código do Plano |
| NomPla | String(100) | Sim | Descrição do Plano |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EveTit | Number(004,0) | Sim | Evento Desconto Titulares |
| EveDep | Number(004,0) | Sim | Evento Desconto Dependentes |
| EveEmp | Number(004,0) | Sim | Evento Parte Empresa |
| RgrTit | Number(003,0) | Sim | Código da Regra Especial do Titular |
| RgrDep | Number(003,0) | Sim | Código da Regra Especial do Dependente |
| RgrEmp | Number(003,0) | Sim | Código da Regra Especial da Empresa |
| TipPla | String(001) | Sim | Tipo do Plano |
| ValIns | Number(011,2) | Sim | Valor Inscrição |
| IntDir | String(001) | Sim | Integrar Valores DIRF |
| IdeDep | Number(003,0) | Sim | Idade Limite Dependente |
| ProPla | Number(001,0) | Sim | Proporcionaliza Mês de Inclusão/Exclusão |
| TipAss | Number(001,0) | Sim | Tipo de Assistência |
| TipAbr | Number(001,0) | Sim | Tipo de abrangência do plano de saúde |
| TipAco | Number(001,0) | Sim | Tipo de acomodação do plano de saúde |

---

## Chave Primária

- CodOem
- CodPla

---

## Índices

### R164PLAIndice2

**Tipo:** Não unico

Campos:
- CodOem
- NomPla

---

## Relacionamentos

### IR_R164PLA_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

