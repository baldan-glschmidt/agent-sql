# R097MOP

## Descrição

Movimentação de Pacientes

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ProPac | String(020) | Não | Prontuário do Paciente |
| Datini | Date | Não | Data Inicial da Internação |
| HorIni | Number(005,0) | Não | Hora Inicial da Internação |
| SeqMov | Number(002,0) | Não | Sequência da Movimentação do Paciente |
| ObsMov | String(080) | Sim | Observação da Movimentação |
| CodPlt | Number(005,0) | Sim | Código do Site |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| DatMov | Date | Sim | Data Movimentação do Paciente |
| HorMov | Number(005,0) | Sim | Hora Movimentação do Paciente |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |

---

## Chave Primária

- ProPac
- Datini
- HorIni
- SeqMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097MOP_002

**Tabela:** R097INT

| Origem | Destino |
|--------|---------|
| ProPac | ProPac |
| Datini | Datini |
| HorIni | HorIni |

