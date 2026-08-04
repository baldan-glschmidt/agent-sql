# E900HOO

## Descrição

O.P./O.S. - Horários Ocupados por O.Ps./O.Ss.

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código Filial de Produção |
| CodEtg | Number(004,0) | Não | Estágio Produção |
| CodCre | String(008) | Não | Código do Centro de Recursos |
| DatCin | Date | Não | Data |
| SeqOrc | Number(004,0) | Não | Sequência do recurso |
| SeqHoo | Number(004,0) | Não | Sequência do horário de início e fim do dia |
| CodOri | String(003) | Não | Origem do Produto/Serviço na O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| EtgOrp | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência lógica da Operação no Roteiro de Produção |
| HorIni | Number(005,0) | Sim | Hora de início |
| HorFim | Number(005,0) | Sim | Hora de fim |
| TmpAlo | Number(013,4) | Sim | Tempo total da OP alocado na respectiva data |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Atualizou o Registro |
| DatAtu | Date | Sim | Data da Atualização do Registro |
| HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodEtg
- CodCre
- DatCin
- SeqOrc
- SeqHoo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900HOO_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E900HOO_007

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

### IR_E900HOO_008

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900HOO_009

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| EtgOrp | CodEtg |

