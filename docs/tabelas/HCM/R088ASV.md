# R088ASV

## Descrição

Autorização para Saída de Veículos de Usuários

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatLib | Date | Não | Data da Liberação |
| HorLib | Number(005,0) | Não | Hora da Liberação |
| MotAsv | Number(001,0) | Sim | Motivo da Saída |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Autorização |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Autorização |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Autorização |
| DatVal | Date | Sim | Data de Validade da Autorização |
| HorVal | Number(005,0) | Sim | Hora de Validade da Autorização |
| StaAut | Number(001,0) | Sim | Status da Autorização |

---

## Chave Primária

- PlaVei
- DatLib
- HorLib

---

## Índices

### R088ASVIndice2

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

### IR_R088ASV_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

