# R097INT

## Descrição

Histórico de Internação

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ProPac | String(020) | Não | Prontuário do Paciente |
| Datini | Date | Não | Data Inicial da Internação |
| HorIni | Number(005,0) | Não | Hora Inicial da Internação |
| CodTin | Number(003,0) | Sim | Código do Tipo de Internação |
| FlgSPA | String(001) | Sim | Somente Pessoas Autorizadas na Visita do Paciente |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| DPrSai | Date | Sim | Data de Previsão de Saída da Internação |
| HPrSai | Number(005,0) | Sim | Hora da Previsão de Saída da Internação |
| DatFim | Date | Sim | Data Final Real da Internação |
| HorFim | Number(005,0) | Sim | Hora Final Real da Internação |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- ProPac
- Datini
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R097INT_000

**Tabela:** R097PAC

| Origem | Destino |
|--------|---------|
| ProPac | ProPac |

### IR_R097INT_003

**Tabela:** R097TIN

| Origem | Destino |
|--------|---------|
| CodTin | CodTin |

