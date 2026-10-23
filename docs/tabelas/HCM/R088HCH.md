# R088HCH

## Descrição

Histórico de Crachás de Veículos

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTVEI (Acesso On-Line) |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |
| CPFRes | Number(011,0) | Sim | CPF da pessoa que coletou as info. em formulário papel durante a contingência |

---

## Chave Primária

- PlaVei
- DatIni
- HorIni

---

## Índices

### R088HCHIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

---

## Relacionamentos

### IR_R088HCH_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

