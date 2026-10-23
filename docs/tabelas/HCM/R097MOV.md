# R097MOV

## Descrição

Movimentação de Visitas do Paciente

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data de Entrada da Visita do Paciente |
| HorEnt | Number(005,0) | Não | Hora de Entrada da Visita do Paciente |
| SeqEnt | Number(002,0) | Não | Sequência da Entrada da Visita do Paciente |
| ProPac | String(020) | Sim | Prontuário do Paciente |
| DatVal | Date | Sim | Data de Validade da Visita do Paciente |
| HorVal | Number(005,0) | Sim | Hora Validade da Visita |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso da Visita do Paciente |
| TipVis | Number(003,0) | Sim | Tipo da Visita |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Entrada |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
