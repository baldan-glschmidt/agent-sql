# R088AEV

## Descrição

Autorização de Entrada Veículos Usuários

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAev | Date | Não | Data para Autorização da Entrada do Veículo |
| HorAev | Number(005,0) | Não | Hora para Autorização da Entrada do Veículo |
| MotAev | Number(001,0) | Sim | Motivo da Entrada do Veículo |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Autorização |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Autorização |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Autorização |
| DatVal | Date | Sim | Data de Validade da Autorização |
| HorVal | Number(005,0) | Sim | Hora de Validade da Autorização |
| StaAut | Number(001,0) | Sim | Status da Autorização |

---

## Chave Primária

- PlaVei
- DatAev
- HorAev

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AEV_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

