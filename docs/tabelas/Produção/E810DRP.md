# E810DRP

## Descrição

PCP - Dados do C. de Recursos p/ Cálculo Carga

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodPvp | String(008) | Não | Código do Período p/ Considerar Informações do Centro Recursos |
| CodCre | String(008) | Não | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| CodEtg | Number(004,0) | Não | Estágio de Produção onde o Recurso é Utilizado |
| QtdCre | Number(008,2) | Sim | Quantidade de Máquinas/Pessoas (equipamentos diversos) |
| QtdHor | Number(004,2) | Não | Quantidade Diária de horas trabalhadas no Centro de Recursos neste período |
| CreAnt | Number(006,0) | Sim | Quantidade Original de Máquinas/Pessoas (equipamentos diversos) |
| QthAnt | Number(004,2) | Sim | Quantidade diária Original de horas trabalhadas no C. Recursos neste período |
| DatAlt | Date | Sim | Data da Alteração |
| HorAlt | Number(005,0) | Sim | Hora da alteração |
| CodUsu | Number(010,0) | Não | Código do Usuário que Alterou |

---

## Chave Primária

- CodEmp
- CodPvp
- CodCre
- CodEtg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E810DRP_001

**Tabela:** E016PVP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPvp | CodPvp |

### IR_E810DRP_002

**Tabela:** E725CRE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCre | CodCre |

