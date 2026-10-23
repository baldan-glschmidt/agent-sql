# R017PLV

## Descrição

Estrutura de Postos - Plano de Vagas

---

## Resumo

- Campos: 30
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| DesRed | String(040) | Sim | Descrição reduzida do plano de vagas |
| DesDet | String(500) | Sim | Descrição detalhada do plano de vagas |
| DatIni | Date | Sim | Data de início da vigência do plano de vagas |
| DatTer | Date | Sim | Data de término da vigência do plano de vagas |
| ConAfa | String(001) | Sim | Considerar afastamentos na composição do saldo |
| ConRqu | String(001) | Sim | Considerar requisições na composição do saldo |
| ConSva | String(001) | Sim | Considerar solicitações de vagas na composição do saldo |
| RefSld | Number(001,0) | Sim | Data de referência para buscar o saldo do quadro de vagas |
| DiaCar | Number(002,0) | Sim | Dias de carência considerados na contagem do saldo |
| UniTem | Number(001,0) | Sim | Indica a unidade de tempo usada para delimitar a linha do tempo do saldo |
| IntAnt | Number(003,0) | Sim | Indica quanto tempo antes da data de referência o saldo deve ser exibido |
| IntApo | Number(003,0) | Sim | Indica quanto tempo após a data de referência o saldo deve ser exibido |
| VerAdm | Number(001,0) | Sim | Ver Quadro Admissão |
| VerQua | Number(001,0) | Sim | Ver Quadro Transferências |
| PerOcu | Number(002,0) | Sim | Código do perfil padrão para novos postos ocupáveis |
| PerAgr | Number(002,0) | Sim | Código do perfil padrão para novos postos agrupadores |
| CodThp | Number(003,0) | Sim | Hierarquia usada para geração do roteiro de aprovação de propostas |
| ExcPef | String(001) | Sim | Indica se pode excluir o quadro previsto para postos com efetivo |
| SitPlv | Number(001,0) | Sim | Indica a situação do plano de vagas para fins de manutenção |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última alteração no plano de vagas |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração do plano de vagas |
| DiasOco | Number(003,0) | Sim | Qtd. Dias para ocorrência |
| ComPro | Number(004,0) | Sim | Código do Compromisso |
| RegOco | Number(003,0) | Sim | Regra da Ocorrência |
| HieAlt | Number(003,0) | Sim | Hierarquia usada para aprovação de propostas de alteração de quadro |
| AloNPH | Number(001,0) | Sim | Alocar novo Posto na Hierarquia |
| VagTmp | String(001) | Sim | Controlar Vaga Temporária |
| HieVTp | Number(003,0) | Sim | Hierarquia usada para Vagas Temporárias |

---

## Chave Primária

- EstPos
- CodPlv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017PLV_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017PLV_016

**Tabela:** R017PER

| Origem | Destino |
|--------|---------|
| PerOcu | PerPos |

### IR_R017PLV_017

**Tabela:** R017PER

| Origem | Destino |
|--------|---------|
| PerAgr | PerPos |

### IR_R017PLV_018

**Tabela:** R017THP

| Origem | Destino |
|--------|---------|
| CodThp | CodThp |

