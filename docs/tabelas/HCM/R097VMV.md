# R097VMV

## Descrição

Visitantes da Movimentação de Visitas do Paciente

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
| DatEnt | Date | Não | Data de Entrada da Visita do Paciente |
| HorEnt | Number(005,0) | Não | Hora de Entrada da Visita do Paciente |
| SeqEnt | Number(002,0) | Não | Sequência da Entrada da Visita do Paciente |
| SeqVis | Number(002,0) | Não | Sequência do Visitante da Movimentação |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Acompanhante |
| NumDoc | String(020) | Sim | Número do Documento do Acompanhante |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| DatSai | Date | Sim | Data de Saída do Visitante |
| HorSai | Number(005,0) | Sim | Hora de Saída do Visitante |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt
- SeqVis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097VMV_002

**Tabela:** R097MOV

| Origem | Destino |
|--------|---------|
| DatEnt | DatEnt |
| HorEnt | HorEnt |
| SeqEnt | SeqEnt |

