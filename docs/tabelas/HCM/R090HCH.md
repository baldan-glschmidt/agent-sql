# R090HCH

## Descrição

Histórico de Crachás de Visitante

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| NumCra | Number(012,0) | Sim | Número do Crachá do Visitante |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |

---

## Chave Primária

- TipDoc
- NumDoc
- DatIni
- HorIni
- SeqEnt

---

## Índices

### R090HCHIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

---

## Relacionamentos

### IR_R090HCH_001

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

