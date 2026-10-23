# R088VCD

## Descrição

Controle de Carga e Descarga de Veículos

---

## Resumo

- Campos: 38
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatChg | Date | Não | Data de Chegada do Veículo |
| HorChg | Number(005,0) | Não | Hora de Chegada do Veículo |
| CodPor | Number(003,0) | Sim | Código da Portaria |
| TipOpe | Number(001,0) | Sim | Tipo de Operação (Carga/Descarga) |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Motorista |
| NumDoc | String(020) | Sim | Número do Documento do Motorista |
| NomMot | String(040) | Sim | Nome Motorista do Veículo |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| PesVei | String(001) | Sim | Pesa Veículo |
| DatLib | Date | Sim | Data Liberação |
| HorLib | Number(005,0) | Sim | Hora Liberação |
| EmpLib | Number(004,0) | Sim | Código da Empresa do Liberador da Entrada |
| TipLib | Number(001,0) | Sim | Tipo de Colaborador do Liberador da Entrada |
| CadLib | Number(009,0) | Sim | Cadastro do Liberador da Entrada |
| NumSen | Number(009,0) | Sim | Número da Senha de Chegada |
| ObsVcd | String(080) | Sim | Observação da Movimentação de Carga e Descarga |
| EmpChg | Number(004,0) | Sim | Código da Empresa do Responsável pelo Cadastro da Chegada |
| TipChg | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Cadastro da Chegada |
| CadChg | Number(009,0) | Sim | Cadastro do Responsável pelo Cadastro de Chegada |
| DatVal | Date | Sim | Data de Validade |
| HorVal | Number(005,0) | Sim | Hora da Validade do Visitante |
| CodPrm | Number(005,0) | Sim | Código Permissão de Acesso |
| StaPng | Number(001,0) | Sim | Status da Chegada |
| MotLib | String(080) | Sim | Motivo da Liberação da Chegada |
| StaChg | Number(001,0) | Sim | Status do registro de chegada do veículo |
| CodLib | Number(002,0) | Sim | Código do motivo da liberação de acesso. |
| UtiAlf | String(001) | Sim | Utiliza área alfandegária. |
| CodMot | Number(004,0) | Sim | Código Motivo Acesso |
| PlaCar | String(010) | Sim | Placa Reboque 1 |
| NumCnh | String(020) | Sim | Número de Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Primeira Habilitação |
| VenCnh | Date | Sim | Data de Vencimento da Carteira de Habilitação |
| PlaCE2 | String(010) | Sim | Placa Reboque 2 |
| PlaCE3 | String(010) | Sim | Placa Reboque 3 |

---

## Chave Primária

- PlaVei
- DatChg
- HorChg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VCD_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

