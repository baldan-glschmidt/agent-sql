# R005VTE

## Descrição

Veículos de Terceiros

---

## Resumo

- Campos: 27
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAci | Number(005,0) | Não | Código do Acidente |
| CodSeq | Number(002,0) | Não | Código da Sequência |
| TipTPv | Number(002,0) | Sim | Tipo de Veículo |
| MarVei | String(015) | Sim | Marca do Veículo |
| ModVei | String(015) | Sim | Modelo do Veículo |
| PlaVei | String(010) | Sim | Placa do Veículo |
| AnoVei | Number(004,0) | Sim | Ano do Veículo |
| NomCon | String(040) | Sim | Nome do Condutor |
| EndCon | String(040) | Sim | Endereço do Condutor |
| TelCon | String(020) | Sim | Telefone do Condutor |
| NumHab | String(020) | Sim | Número da Habilitação do Motorista |
| ValHab | Date | Sim | Validade da Habilitação do Motorista |
| CatHab | String(010) | Sim | Categorias da Habilitação do Motorista |
| EstFis | Number(001,0) | Sim | Estado Físico do Motorista |
| ExaDia | String(001) | Sim | Exames Médicos em Dia |
| UsaCin | String(001) | Sim | Usava Cinto de Segurança |
| DosAlc | String(001) | Sim | Submetido a Exame de Dosagem Alcoólica |
| EvaLoc | String(001) | Sim | Evadiu-se do Local do Acidente |
| NomPro | String(040) | Sim | Nome do Proprietário do Veículo |
| EndPro | String(040) | Sim | Endereço do Proprietário do Veículo |
| TelPro | String(020) | Sim | Telefone do Proprietário do Veículo |
| DesAva | String(2500) | Sim | Descrição das Avarias no Veículo |
| ObsVTe | String(2500) | Sim | Observação do Veículo |
| DddCon | Number(003,0) | Sim | Código DDD do condutor |
| DddPro | Number(003,0) | Sim | Código DDD do proprietário |
| DdiCon | Number(003,0) | Sim | Código DDI do condutor |
| DdiPro | Number(003,0) | Sim | Código DDI do proprietário |

---

## Chave Primária

- CodAci
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005VTE_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

