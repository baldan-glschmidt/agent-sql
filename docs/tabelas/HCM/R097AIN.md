# R097AIN

## Descrição

Acompanhante da Internação

---

## Resumo

- Campos: 12
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
| SeqAco | Number(004,0) | Não | Sequência do Acompanhante da Internação |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Acompanhante |
| NumDoc | String(020) | Sim | Número do Documento do Acompanhante |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| DatIAc | Date | Sim | Data Início Acompanhamento |
| HorIAc | Number(005,0) | Sim | Hora Inicial Acompanhamento |
| DatFAc | Date | Sim | Data Final do Acompanhamento |
| HorFAc | Number(005,0) | Sim | Hora Final Real do Acompanhamento |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- ProPac
- Datini
- HorIni
- SeqAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097AIN_002

**Tabela:** R097INT

| Origem | Destino |
|--------|---------|
| ProPac | ProPac |
| Datini | Datini |
| HorIni | HorIni |

