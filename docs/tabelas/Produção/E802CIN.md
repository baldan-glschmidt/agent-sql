# E802CIN

## Descrição

PCP - Calendário Industrial

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código Filial de Produção |
| CodEtg | Number(004,0) | Não | Estágio Produção |
| CodCre | String(008) | Não | Código do Centro de Recursos |
| DatCin | Date | Não | Data |
| DurDia | Number(006,2) | Sim | Percentual em relação a quantidade horas de trabalho do dia (quando calendário p/ o estágio) |
| DiaSem | String(013) | Não | Dia da Semana |
| QtdHor | Number(004,2) | Sim | Quantidade de horas do dia de trabalho (quando calendário p/ Recurso) |
| CodUsu | Number(010,0) | Não | Código do Usuário que Atualizou o Registro |
| DatAtu | Date | Sim | Data da Atualização do Registro |
| HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro |
| QtdCre | Number(008,2) | Sim | Quantidades de Recursos disponível neste dia (Quando cal. p/ Recurso) |

---

## Chave Primária

- CodEmp
- CodFil
- CodEtg
- CodCre
- DatCin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E802CIN_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

