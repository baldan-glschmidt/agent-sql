# R097AUP

## Descrição

Autorização de Pessoas

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
| ProPac | String(020) | Não | Prontuário do Paciente |
| Datini | Date | Não | Data Inicial da Internação |
| HorIni | Number(005,0) | Não | Hora Inicial da Internação |
| SeqPes | Number(002,0) | Não | Sequência da Pessoa da Autorização |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Acompanhante |
| NumDoc | String(020) | Sim | Número do Documento do Acompanhante |
| NomPes | String(040) | Sim | Nome da Pessoa Autorizada |
| MotPna | String(059) | Sim | Motivo da Autorização |
| FlgAut | String(001) | Sim | Pessoa Autorizada |

---

## Chave Primária

- ProPac
- Datini
- HorIni
- SeqPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097AUP_002

**Tabela:** R097INT

| Origem | Destino |
|--------|---------|
| ProPac | ProPac |
| Datini | Datini |
| HorIni | HorIni |

