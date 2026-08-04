# E900ORC

## Descrição

O.P./O.S. - Ocupação dos Recursos no Calendário Industrial

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
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
| SeqOrc | Number(004,0) | Não | Seqüência do recurso |
| QtdHor | Number(004,2) | Sim | Quantidade de horas do dia de trabalho |
| TmpLiv | Number(013,4) | Sim | Tempo total livre do recurso na respectiva data |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Atualizou o Registro |
| DatAtu | Date | Sim | Data da Atualização do Registro |
| HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro |
| HorIni | Number(005,0) | Sim | Hora de início previsto conforme intervalos dos turnos (E803HTR) |
| HorFim | Number(005,0) | Sim | Hora de fim previsto conforme intervalos dos turnos (E803HTR) |

---

## Chave Primária

- CodEmp
- CodFil
- CodEtg
- CodCre
- DatCin
- SeqOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900ORC_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

