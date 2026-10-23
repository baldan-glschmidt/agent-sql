# R088PVT

## Descrição

Programação de Veículos de Teste

---

## Resumo

- Campos: 51
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MarVei | String(015) | Não | Marca do Veículo |
| ModVei | String(015) | Não | Modelo do Veículo |
| NumCha | String(020) | Não | Número do Chassi |
| DatLib | Date | Não | Data da Liberação |
| HorLib | Number(005,0) | Não | Hora da Liberação |
| EmpCon | Number(004,0) | Sim | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Sim | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Sim | Cadastro do Condutor |
| DatCon | Date | Sim | Data de Retorno do Condutor |
| HorCon | Number(005,0) | Sim | Hora do Retorno do Condutor |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Programação |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Programação |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Programação |
| QuiSai | Number(007,0) | Sim | Quilometragem do Veículo na Saída Portaria |
| AceNor | String(001) | Sim | Equipamentos Obrigatórios |
| ObsMov | String(080) | Sim | Observação do Movimento |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |
| DatRet | Date | Sim | Data de Retorno do Veículo |
| HorRet | Number(005,0) | Sim | Hora do Retorno Veículo |
| TipRet | Number(001,0) | Sim | Tipo de Retorno |
| NumNFV | Number(007,0) | Sim | Número da Nota Fiscal do Veículo |
| DatNFV | Date | Sim | Data da Nota Fiscal do Veículo |
| NumDut | Number(009,0) | Sim | Número do Dut do Veículo |
| LocTes | String(030) | Sim | Local de Testes do Veículo |
| TemRom | String(001) | Sim | Tem Romaneio |
| ConCom | String(001) | Sim | Tem Contrato de Comodato |
| QtdDias | Number(003,0) | Sim | Qtde de Dias do Comodato |
| NFSCom | Number(007,0) | Sim | Número da Nota Fiscal do Comodato |
| PlaVei | String(010) | Sim | Placa do Veículo |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do  Local |
| NumLoc | Number(009,0) | Sim | Local da Unidade de Testes |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Programação |
| QuiRet | Number(007,0) | Sim | Quilometragem do Veículo no Retorno |
| EmpRsp | Number(004,0) | Sim | Código da Empresa do Responsável Retorno |
| TclRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Retorno |
| CadRsp | Number(009,0) | Sim | Cadastro do Responsável pelo Retorno |
| EmpSai | Number(004,0) | Sim | Código da Empresa do Responsável pela Saída |
| TclSai | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Saída |
| CadSai | Number(009,0) | Sim | Cadastro do Responsável pela Saída |
| EmpSeg | Number(004,0) | Sim | Código da Empresa do Condutor de Retorno do Veículo |
| TclSeg | Number(001,0) | Sim | Tipo de Colaborador do Condutor de Retorno de Veículo |
| CadSeg | Number(009,0) | Sim | Cadastro do Condutor de Retorno do Veículo |
| DatSeg | Date | Sim | Data de Retorno do Condutor |
| HorSeg | Number(005,0) | Sim | Hora do Retorno do Condutor |
| DatPla | Date | Sim | Data de Retorno da Placa |
| HorPla | Number(005,0) | Sim | Hora do Retorno da Placa |
| DatTra | Date | Sim | Data de Retorno do Veículo Transportado |
| HorTra | Number(005,0) | Sim | Hora do Retorno do Veículo Transportado |
| PorSai | Number(003,0) | Sim | Código da Portaria de Saída |
| PorRet | Number(003,0) | Sim | Código da Portaria de Retorno |

---

## Chave Primária

- MarVei
- ModVei
- NumCha
- DatLib
- HorLib

---

## Índices

### R088PVTIndice2

**Tipo:** Não unico

Campos:
- EmpCon
- TClCon
- CadCon

### R088PVTIndice3

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

### IR_R088PVT_000

**Tabela:** R088MAR

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |

### IR_R088PVT_001

**Tabela:** R088MOD

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |
| ModVei | ModVei |

### IR_R088PVT_002

**Tabela:** R088VET

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |
| ModVei | ModVei |
| NumCha | NumCha |

### IR_R088PVT_029

**Tabela:** R088PLT

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

