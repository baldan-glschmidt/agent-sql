# R088VEF

## Descrição

Veículos da Frota

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data Inicial do Uso do Veículo |
| DatFim | Date | Sim | Data Final para Utilização do Veículo |
| EmpVei | Number(004,0) | Sim | Empresa Proprietária do Veículo |
| VeiLoc | String(001) | Sim | Veículo Locado |
| EmpLoc | Number(008,0) | Sim | Código da Outra Empresa (Terceiro/Parceiro) |
| ConLoc | String(015) | Sim | Número do Contrato de Locação |
| NumEmp | Number(004,0) | Sim | Empresa do Colabolador Responsável pelo Veículo |
| TipCol | Number(001,0) | Sim | Tipo do Colabolador Responsável pelo Veículo |
| NumCad | Number(009,0) | Sim | Cadastro do Colabolador Responsável pelo Veículo |

---

## Chave Primária

- PlaVei
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VEF_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

