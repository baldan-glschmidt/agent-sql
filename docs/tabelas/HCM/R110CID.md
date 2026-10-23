# R110CID

## Descrição

Atendimentos - CID-10

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| CodDoe | String(004) | Não | Classificação Internacional de Doenças |
| CodSub | String(003) | Não | Identificação do subgrupo da CID-10 |
| PriDef | String(001) | Sim | Indicador da principal doença |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| EstCid | Number(001,0) | Sim | Estado do Diagnóstico |
| SitCid | Number(001,0) | Sim | Situação Atual do Diagnóstico |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- CodDoe
- CodSub

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110CID_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

