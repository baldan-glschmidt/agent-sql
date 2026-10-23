# R005ACI

## Descrição

Acidentes de Trânsito

---

## Resumo

- Campos: 45
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAci | Number(005,0) | Não | Código do Acidente |
| DatAci | Date | Sim | Data do Acidente |
| HorAci | Number(005,0) | Sim | Hora do Acidente |
| NumBol | String(010) | Sim | Número do Boletim de Ocorrência |
| DatAvi | Date | Sim | Data de Aviso |
| HorAvi | Number(005,0) | Sim | Hora de Aviso |
| CodTCo | Number(002,0) | Sim | Código do Tipo de Colisão |
| EmpLin | Number(004,0) | Sim | Empresa da Linha |
| CodLin | Number(004,0) | Sim | Código da Linha |
| PlaVei | String(010) | Sim | Inutilizado |
| QtdFer | Number(003,0) | Sim | Quantidade de Passageiros Feridos |
| DesAci | String(2500) | Sim | Descrição do Acidente |
| DesAva | String(2500) | Sim | Descrição das Avarias no Acidente |
| RuaAci | String(040) | Sim | Rua do Acidente |
| NumAci | Number(005,0) | Sim | Número na Rua do Acidente |
| CidAci | Number(007,0) | Sim | Cidade do Acidente |
| BaiAci | Number(004,0) | Sim | Bairro do Acidente |
| ZonAci | Number(001,0) | Sim | Zona da Cidade |
| PrxAci | String(060) | Sim | Proximidades |
| LeiVia | Number(001,0) | Sim | Tipo de Leito da Via |
| ConVia | Number(001,0) | Sim | Condição da Via |
| SntVia | Number(001,0) | Sim | Sentido da Via |
| ConTem | Number(001,0) | Sim | Condição do Tempo |
| ConLum | Number(001,0) | Sim | Condição de Luminosidade |
| CarTer | Number(001,0) | Sim | Características do Terreno |
| EmpMot | Number(004,0) | Sim | Empresa do Motorista |
| TipMot | Number(001,0) | Sim | Tipo do Motorista |
| CadMot | Number(009,0) | Sim | Cadastro do Motorista |
| EstMot | Number(001,0) | Sim | Estado Físico do Motorista |
| ExaDia | String(001) | Sim | Exames Médicos em Dia |
| UsaCin | String(001) | Sim | Usava Cinto de Segurança |
| DosAlc | String(001) | Sim | Submetido a Exame de Dosagem Alcoólica |
| EvaLoc | String(001) | Sim | Evadiu-se do Local |
| MotFer | String(001) | Sim | Motorista Ferido |
| NomPer | String(040) | Sim | Nome do Perito |
| MotCul | String(001) | Sim | Motorista Culpado |
| PodEvi | String(001) | Sim | Motorista Poderia Ter Evitado o Acidente |
| EmpRes | Number(004,0) | Sim | Empresa do Responsável |
| TclRes | Number(001,0) | Sim | Tipo do Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável |
| EmpFis | Number(004,0) | Sim | Empresa do Fiscal |
| TClFis | Number(001,0) | Sim | Tipo do Fiscal |
| CadFis | Number(009,0) | Sim | Cadastro do Fiscal |
| ParFis | String(2500) | Sim | Parecer do Fiscal |
| NumVei | Number(006,0) | Sim | Número do Veículo |

---

## Chave Primária

- CodAci

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005ACI_006

**Tabela:** R005TCO

| Origem | Destino |
|--------|---------|
| CodTCo | CodTCo |

