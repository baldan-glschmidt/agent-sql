# R097FOT

## Descrição

Foto do Paciente

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ProPac | String(020) | Não | Prontuário do Paciente |
| FotPac | Image | Sim | Foto do Paciente |
| DatFot | Date | Sim | Data da Foto |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- ProPac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097FOT_000

**Tabela:** R097PAC

| Origem | Destino |
|--------|---------|
| ProPac | ProPac |

