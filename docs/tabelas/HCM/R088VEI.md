# R088VEI

## Descrição

Veículos

---

## Resumo

- Campos: 37
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| EstPla | String(002) | Sim | Unidade da Federação na Placa do Veículo |
| MarVei | String(015) | Sim | Marca do Veículo |
| ModVei | String(015) | Sim | Modelo do Veículo |
| CorVei | String(015) | Sim | Cor do Veículo |
| AnoVei | Number(004,0) | Sim | Ano de Fabricação do Veículo |
| AnoMod | Number(004,0) | Sim | Ano do Modelo do Veículo |
| TipVei | Number(002,0) | Sim | Tipo de Veículo e Espécie Contram |
| QtdPas | Number(002,0) | Sim | Quantidade Permitida de Passageiros |
| PesVei | Number(006,0) | Sim | Peso do Veículo |
| CapCar | Number(006,0) | Sim | Capacidade de Carga do Veículo |
| VenLic | Number(002,0) | Sim | Mês Vencimento da Licença (IPVA) e Seguro Obrigatório |
| VenSeg | Number(002,0) | Sim | Mês Vencimento do Seguro |
| NumCha | String(020) | Sim | Número do Chassi |
| NumMot | String(020) | Sim | Número do Motor |
| ObsVei | String(1500) | Sim | Observação do Veículo |
| SitVei | Number(003,0) | Sim | Situação do Veículo |
| VeiPol | String(001) | Sim | Veículo é de Uso Geral (Pool) |
| TipCmb | Number(002,0) | Sim | Tipo de Combustível |
| NumImb | String(010) | Sim | Número do Ativo Fixo Imobilizado |
| TrpPrv | Date | Sim | Tempo previsto para troca de veículo |
| NumRen | String(011) | Sim | Código Renavam (Documento do Veículo) |
| CodOri | Number(007,0) | Sim | Código da Cidade de Origem do Veículo |
| QuiVei | Number(007,0) | Sim | Quilometragem do Veículo |
| UsaChk | String(001) | Sim | Veículo Usa Controle de Manutenção |
| NumVei | Number(006,0) | Sim | Número do Veículo |
| FotVei | Image | Sim | Foto Veículo |
| GerPor | Number(001,0) | Sim | Veículo gerenciado por |
| IdeVis | String(010) | Sim | Código de Identificação Visual do Veículo |
| IntBDC | String(001) | Sim | Integra Outra Empresa com Controle Alfandegado |
| DatInc | Date | Sim | Data Integração BDCC |
| HorInc | Number(005,0) | Sim | Hora Integração BDCC |
| StaBDC | Number(001,0) | Sim | Status BDCC |
| PrpVei | Number(001,0) | Sim | Proprietário do Veículo para o Controle Alfandegado |
| TpoVei | String(004) | Sim | Tipo de Veículo Alfandegado |
| RgAntt | String(020) | Sim | Registro ANTT |
| ConLPR | String(001) | Sim | Participa do Controle LPR |

---

## Chave Primária

- PlaVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
