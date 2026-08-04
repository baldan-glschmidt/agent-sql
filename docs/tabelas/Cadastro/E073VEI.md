# E073VEI

## Descrição

Cadastros - Transportadoras - Veículos

---

## Resumo

- Campos: 44
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| PlaVei | String(010) | Não | Placa do veículo |
| UfsVei | String(002) | Não | Sigla do estado do veículo |
| CepVei | Number(008,0) | Sim | CEP da cidade do veículo |
| CodMar | Number(004,0) | Não | Código da marca do veículo |
| CodMod | Number(004,0) | Não | Código do modelo do veículo |
| AnoVei | String(010) | Sim | Ano do veículo |
| CodCor | Number(004,0) | Não | Código da Cor |
| CodTip | Number(004,0) | Não | Código do tipo de veículo |
| PesMax | Number(011,2) | Sim | Peso Máximo |
| NumCer | String(030) | Sim | Certificado do Proprietário |
| ChaVei | String(050) | Sim | Chassi do veículo |
| CodVia | String(003) | Não | Código da via de transporte do veículo |
| ClaVei | String(001) | Sim | Classificação do veículo |
| DatCom | Date | Sim | Data da compra do veículo |
| DatVen | Date | Sim | Data da Venda do Veículo |
| SitVei | String(001) | Não | Situação do veículo |
| TarVei | Number(011,2) | Sim | Tara do veículo |
| NumRen | String(020) | Sim | Renavam |
| VisIni | Date | Sim | Data início vistoria |
| VisFim | Date | Sim | Data final da vistoria |
| VisVsa | Date | Sim | Data da inspeção do veículo na empresa |
| VolMax | Number(011,2) | Sim | Volume máximo do veículo |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do veículo |
| ObsMot | String(250) | Sim | Observação do motivo da situação |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação |
| DatMot | Date | Sim | Data do motivo da situação |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação |
| SeqCav | Number(006,0) | Sim | Sequência de cadastramento do veículo |
| EenVei | String(018) | Sim | Código do endereço do veículo |
| ForFre | Number(009,0) | Sim | Código do fornecedor para geração título de frete |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CtrEnt | String(001) | Sim | Indicativo se o veículo faz parte do controle de entrega de mercadorias |
| QtdPor | Number(004,0) | Sim | Quantidade portas do veículo para utilizar lacres |
| ProVei | String(001) | Sim | Tipo do proprietário do veículo |
| TipRod | String(002) | Sim | Tipo de rodado do veículo |
| TipCrr | String(002) | Sim | Tipo de carroceria do veículo |
| NrnTrc | String(014) | Sim | Registro nacional de transportadores rodoviários de carga - RNTRC |
| IdePrt | Number(009,0) | Sim | Proprietário do veículo |

---

## Chave Primária

- CodTra
- PlaVei

---

## Índices

### E073VEIIndice1

**Tipo:** Não unico

Campos:
- CodVia

---

## Relacionamentos

### IR_E073VEI_012

**Tabela:** E074VIA

| Origem | Destino |
|--------|---------|
| CodVia | CodVia |

