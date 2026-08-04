# E900OBS

## Descrição

O.P./O.S. - Observações Adicionais da O.P.

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Origem do produto/serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da ordem de produção/serviço |
| SeqObs | Number(004,0) | Não | Sequência numérica da observação |
| TipObs | String(001) | Não | Tipo da observação |
| DesObs | String(240) | Não | Histórico do produto - informativos e/ou detalhes técnicos |
| DatAtu | Date | Sim | Data da atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da atualização do registro |
| CodUsu | Number(010,0) | Não | Código do usuário que atualizou o registro |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900OBS_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

