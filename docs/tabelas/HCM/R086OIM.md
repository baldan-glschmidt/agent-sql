# R086OIM

## Descrição

Ocorrências - Imagens

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| OcoAct | Number(006,0) | Não | Código da Ocorrência |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| DesImg | String(030) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OIM_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

