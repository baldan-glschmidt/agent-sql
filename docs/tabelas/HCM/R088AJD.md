# R088AJD

## Descrição

Ajudantes de  Carga e Descarga de Veículos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatChg | Date | Não | Data e Hora de Chegada do Veículo |
| HorChg | Number(005,0) | Não | Hora de Chegada do Veículo |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Ajudante |
| NumDoc | String(020) | Não | Número do Documento do Ajudante |
| NomAjd | String(040) | Sim | Nome do Ajudante na Carga e Descarga do Veículo |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| NumSen | Number(009,0) | Sim | Número da Senha de Chegada |
| StaPng | Number(001,0) | Sim | Status da Chegada do Ajudante |

---

## Chave Primária

- PlaVei
- DatChg
- HorChg
- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AJD_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

